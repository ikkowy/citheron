<script setup>
import { ref } from "vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

const props = defineProps({
  inverted: Boolean,
  toggle: Boolean
});

const toggled = ref(false);

function toggle_() {
  if (props.toggle) {
    toggled.value = !toggled.value;
  }
}
</script>

<template>
  <button class="click-button" v-bind:class="{ inverted: props.inverted ^ toggled }" v-on:click="toggle_()">
    <slot />
  </button>
</template>

<style scoped>
.click-button {
  position: relative;
  box-sizing: border-box;
  border: none;
  outline: none;
  font-size: 16px;
  padding: 7px 15px;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
}

.click-button:not(.inverted) {
  border: 2px solid v-bind("theme.colFg1");
  background-color: v-bind("theme.colBg1");
  color: v-bind("theme.colFg1");
}

.click-button:not(.inverted):active {
  background-color: v-bind("theme.colFg1");
  color: v-bind("theme.colBg1");
}

.click-button.inverted {
  border: 2px solid v-bind("theme.colFg1");
  background-color: v-bind("theme.colFg1");
  color: v-bind("theme.colBg1");
}

.click-button.inverted:active {
  background-color: v-bind("theme.colBg1");
  color: v-bind("theme.colFg1");
}
</style>
