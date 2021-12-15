<template>
  <Map :snappedPoints="snappedPoints" :points="points" />
  <div class="container">
    <div class="row">
      <div class="col-lg-10 col-12">
        <Form>
          <div class="row flex-row">
            <div class="col-lg-6 col-12">
              <Input
                v-for="adress in addresses"
                :key="addresses.indexOf(adress)"
                v-model="adress.value"
                InputClass="TestInput mb-2"
              />
            </div>
            <div class="col-lg-3 col-12">
              <div class="input-buttons">
                <Button
                  @click="addInput"
                  ButtonClass="mb-2"
                  ButtonText="Добавить адрес"
                />
                <Button
                  @click="removeInput"
                  ButtonClass="mb-2"
                  ButtonText="Убрать адрес"
                />
              </div>
              <div class="confirm-btn mt-4">
                <Button
                  @click="getPoints"
                  ButtonClass="ConfirmButton mb-2"
                  ButtonText="Создать маршрут"
                />
              </div>
            </div>
            <div class="col-lg-3 col-12">
              <p class="total-duration text-center">
                Суммарное время маршрута:<br />
                {{ totalDuration }}
              </p>
            </div>
          </div>
        </Form>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { API_KEY } from "./constance";
import Input from "./components/Input.vue";
import Button from "./components/Button.vue";
import Form from "./components/Form.vue";
import Map from "./components/Map.vue";

export default {
  name: "App",
  components: {
    Button,
    Input,
    Form,
    Map,
  },
  mounted() {},
  data() {
    return {
      addresses: [{ value: "" }, { value: "" }],
      points: [],
      snappedPoints: [],
      totalDuration: "",
    };
  },
  methods: {
    getTimeFromMins(sec) {
      let hours = Math.floor(sec / 60 / 60);
      let minutes = Math.floor(sec / 60) - hours * 60;
      let seconds = sec % 60;
      return hours + " часов " + minutes + " минут " + seconds + " секунд.";
    },
    removeInput() {
      if (this.addresses.length < 3) alert("Минимальное количество точек: 2");
      else this.addresses.pop();
    },
    addInput() {
      if (this.addresses.length < 8) this.addresses.push({ value: "" });
      else alert("Максимальное количество точек: 8");
    },
    getPoints() {
      if (
        this.addresses.filter((item) => {
          return item.value == "";
        }).length > 0
      )
        alert("Пустая строка.");
      else {
        const fetchPoints = new Promise((resolve) => {
          this.addresses.forEach((element) => {
            axios
              .get("https://maps.googleapis.com/maps/api/geocode/json", {
                params: {
                  address: element.value,
                  key: API_KEY,
                },
              })
              .then((response) => {
                let point = {
                  position: response.data.results[0].geometry.location,
                };
                if (
                  this.points.filter((item) => {
                    return (
                      point.position.lat == item.position.lat &&
                      point.position.lng == item.position.lng
                    );
                  }).length > 0
                ) {
                  alert("Такая точка существует.");
                } else {
                  this.points.push(point);
                }
              });
          });
          resolve("success");
        });
        fetchPoints.then(() => {
          window.localStorage.setItem("point", JSON.stringify(this.points));
          this.getPolylinePaths();
        });
      }
    },
    getPolylinePaths() {
      axios
        .get("http://127.0.0.1:5000/points", {
          params: {
            origin: this.addresses[0].value,
            language: "ru",
            waypoints: this.getWaypoints(),
            destination: this.addresses[this.addresses.length - 1].value,
            key: API_KEY,
          },
        })
        .then((response) => {
          this.$gmapApiPromiseLazy().then(() => {
            // eslint-disable-next-line no-undef
            let paths = google.maps.geometry.encoding.decodePath(
              response.data.routes[0].overview_polyline.points
            );
            paths.forEach((element) => {
              this.snappedPoints.push({
                location: { lat: element.lat(), lng: element.lng() },
              });
            });
          });
          let totalTime = 0;
          response.data.routes[0].legs.forEach((element) => {
            totalTime += parseInt(element.duration.value);
          });
          this.totalDuration = this.getTimeFromMins(totalTime);
        });
    },
    getWaypoints() {
      let waypointsObject = this.addresses.slice(1, -1);
      if (waypointsObject.length == 0) return "";
      else {
        let waypointsArray = [];
        waypointsObject.forEach((element) => {
          waypointsArray.push(element.value);
        });
        return "optimize:true|" + waypointsArray.join("|");
      }
    },
  },
};
</script>

<style lang="sass">
.vue-map-container
    height: 500px
.flex-row
    width: 100%
.TestInput
    width: 100%
.ConfirmButton
    background: green !important
</style>
