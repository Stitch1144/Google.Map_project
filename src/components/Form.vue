<template>
    <div class="form-container">
        <form @submit.prevent class="form-wrapper">
            <slot></slot>
        </form>
    </div>
</template>

<script>
export default {
    name: "Form",
};
</script>

<style lang="sass" scoped>
.form
    &-wrapper
        display: flex
        flex-direction: column
        padding: 15px
        align-items: center
</style>
