<script setup>
import { computed, ref } from "vue";

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
     :style="floatStyle"
     @mouseover="hovered = true"
     @mouseleave="hovered = false"
     :class="{ 'active': props.active }">
    <iwy-icon v-bind:name="props.icon" />
    <span v-if="counterText">{{ counterText }}</span>
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
  background-color: v-bind("theme.colBg");
  cursor: pointer;
}

.header-button:hover {
  background-color: v-bind("theme.colFg");
}

.header-button svg {
  display: block;
  margin: auto;
  width: 70%;
  fill: v-bind("theme.colFg");
}

.header-button:hover svg {
  fill: v-bind("theme.colBg");
}

.header-button span {
  box-sizing: border-box;
  position: absolute;
  right: 2px;
  bottom: 2px;
  padding: 1px 2px;
  background-color: v-bind("theme.colRed");
  color: white;
  font-size: 10px;
  font-weight: bold;
  border-radius: 15%;
  user-select: none;
}

.header-button.active {
  background-color: v-bind("theme.colFg");
}

.header-button.active svg {
  fill: v-bind("theme.colBg");
}
</style>
