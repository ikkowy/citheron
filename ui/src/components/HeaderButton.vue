<script setup>
import { computed, defineProps, ref } from "vue";

import IconElement from "./IconElement.vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

const props = defineProps({
  icon: String,
  float: {
    type: String,
    default: "left",
    validator(value) {
      return ["left", "right"].includes(value);
    }
  },
  counter: {
    required: false
  },
  active: {
    type: Boolean,
    default: false
  }
});

const floatStyle = computed(() => {
  return `float: ${props.float}`;
});

const counterText = computed(() => {
  let value = parseInt(props.counter);
  if (isNaN(value) || value < 1)
    return null;
  if (value > 99)
    return "∞";
  return `${value}`;
});

const hovered = ref(false);

const backgroundColor = computed(() => {
  return props.active || hovered.value ? theme.headerHoverBackgroundColor : theme.headerBackgroundColor;
});
</script>

<template>
  <a class="header-button" v-bind:style="floatStyle" v-on:mouseover="hovered = true" v-on:mouseleave="hovered = false">
    <IconElement v-bind:name="props.icon" />
    <span v-if="counterText">{{ counterText }}</span>
  </a>
</template>

<style scoped>
.header-button {
  position: relative;
  display: flex;
  align-items: center;
  height: 100%;
  aspect-ratio: 1 / 1;
  background-color: v-bind(backgroundColor);
  cursor: pointer;
}

.header-button svg {
  display: block;
  margin: auto;
  width: 70%;
  fill: v-bind("theme.headerForegroundColor");
}

.header-button span {
  position: absolute;
  box-sizing: border-box;
  right: 2px;
  bottom: 2px;
  padding: 1px 2px;
  background-color: v-bind("theme.headerMenuButtonCounterBackgroundColor");
  color: v-bind("theme.headerMenuButtonCounterForegroundColor");
  font-size: 10px;
  font-weight: bold;
  border-radius: 15%;
  user-select: none;
}
</style>
