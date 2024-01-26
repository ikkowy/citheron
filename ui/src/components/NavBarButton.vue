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
</script>

<template>
  <a class="header-button"
      v-bind:style="floatStyle"
      v-on:mouseover="hovered = true"
      v-on:mouseleave="hovered = false"
      v-bind:class="{ 'active': props.active }">
    <IconElement v-bind:name="props.icon" />
    <span v-if="counterText">{{ counterText }}</span>
    <a class="active-dash"></a>
  </a>
</template>

<style scoped>
.header-button {
  box-sizing: border-box;
  position: relative;
  display: flex;
  align-items: center;
  height: 100%;
  aspect-ratio: 1 / 1;
  background-color: v-bind(backgroundColor);
  cursor: pointer;
}

.header-button:hover {
  background-color: v-bind("theme.headerHoverBackgroundColor");
}

.header-button svg {
  display: block;
  margin: auto;
  width: 70%;
  fill: v-bind("theme.headerForegroundColor");
}

.header-button span {
  box-sizing: border-box;
  position: absolute;
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

.header-button.active {
  background-color: v-bind("theme.headerHoverBackgroundColor");
}

.header-button .active-dash {
  position: absolute;
  width: 100%;
  height: 2px;
  bottom: 0;
  background-color: v-bind("props.active ? theme.headerForegroundColor : 'transparent'");
}
</style>
