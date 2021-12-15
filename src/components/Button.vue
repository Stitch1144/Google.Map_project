<template>
    <div class="button-container">
        <button :class="ButtonClass" class="button" :type="ButtonType">
            {{ ButtonText }}
        </button>
    </div>
</template>

<script>
export default {
    props: {
        ButtonType: { type: String, default: "button" },
        ButtonClass: { type: String, required: false },
        ButtonText: { type: String, required: true },
    },
};
</script>

<style lang="sass" scoped>
.button
    background: #fff
    border: 1px solid #2a582a
    padding: 5px 15px
    border-radius: 10px
    &:hover
        opacity: 0.8
        background: #2a582a
        border: 1px solid #fff
</style>
