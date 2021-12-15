<template>
  <div class="input-wrapper">
    <GMapAutocomplete
      :placeholder="InputPlaceholder"
      :class="InputClass"
      @place_changed="$emit('update:modelValue', $event.formatted_address)"
      :value="modelValue"
      class="input"
      @input="$emit('update:modelValue', $event.target.value)"
    >
    </GMapAutocomplete>
  </div>
</template>

<script>
export default {
  name: "Input",
  props: {
    modelValue: String,
    InputClass: { type: String, required: false },
    InputPlaceholder: { type: String, default: "Введите адрес" },
  },
};
</script>

<style lang="sass" scoped>
.input
    padding: 10px 15px
    border: 1px solid #2a582a !important
    border-radius: 15px
    min-width: 40%
    &:focus
        outline: none
</style>
