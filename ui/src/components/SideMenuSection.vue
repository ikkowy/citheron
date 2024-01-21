<script setup>
import { defineProps } from "vue";

const props = defineProps({
  name: String,
  caption: String,
  back: String
});
</script>

<template>
  <div class="side-menu-section"
       v-bind:data-side-menu-section-name="props.name"
       v-bind:data-side-menu-section-caption="props.caption"
       v-bind:data-side-menu-section-back="props.back">
    <slot />
  </div>
</template>

<style scoped>
</style>
