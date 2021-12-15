<template>
  <div class="map" id="map">
    <GMapMap
      :center="center"
      :zoom="15"
      map-type-id="terrain"
      style="width: 500px; height: 300px"
    >
      <GMapMarker
        :position="point.position"
        :key="points.indexOf(point)"
        v-for="point in points"
      />

      <GMapPolyline :options="options" :path="getPath" ref="polyline" />
    </GMapMap>
  </div>
</template>

<script>
export default {
  name: "Map",
  props: {
    points: Array,
    snappedPoints: Object,
  },
  data() {
    return {
      center: { lat: 47.2230894, lng: 39.7177804 },
      options: {
        strokeColor: "red",
        strokeOpacity: 0.8,
        strokeWeight: 3,
        fillColor: "#FFF",
        fillOpacity: 0.35,
      },
      markers: [
        {
          position: {
            lat: 51.093048,
            lng: 6.84212,
          },
        },
      ],
    };
  },
  computed: {
    setCenter() {
      return this.snappedPoints.location[0];
    },
    getPath() {
      let arr = [];
      for (let i = 0; i < this.snappedPoints.length; i++) {
        arr.push(this.snappedPoints[i].location);
      }
      return arr;
    },
  },
};
</script>

<style></style>
