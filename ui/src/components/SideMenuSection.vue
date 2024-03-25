<script setup>
const props = defineProps({
  name: String,
  caption: String,
  back: String
});
</script>

<template>
  <div
      class="side-menu-section"
      :data-side-menu-section-name="props.name"
      :data-side-menu-section-caption="props.caption"
      :data-side-menu-section-back="props.back">
    <slot></slot>
  </div>
</template>

<style scoped>
</style>
