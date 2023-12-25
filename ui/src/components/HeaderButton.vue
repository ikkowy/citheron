<script setup>
import { computed, defineProps } from "vue";

import IconElement from "./IconElement.vue";

import { theme } from "../theme.js";

const props = defineProps({
  icon: String,
  float: {
    type: String,
    default: "left",
    validator(value) {
      return ["left", "right"].includes(value);
    }
  }
});

const floatStyle = computed(() => {
  return `float: ${props.float}`;
});
</script>

<template>
  <a class="header-button" v-bind:style="floatStyle">
    <IconElement v-bind:name="props.icon" />
  </a>
</template>

<style scoped>
.header-button {
  display: flex;
  align-items: center;
  height: 100%;
  aspect-ratio: 1 / 1;
}

.header-button:hover {
  cursor: pointer;
  background-color: v-bind("theme.headerHoverBackgroundColor");
}

.header-button svg {
  display: block;
  margin: auto;
  width: 70%;
  fill: v-bind("theme.headerForegroundColor");
}
</style>
