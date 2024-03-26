<script setup>
import { ref } from "vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

const props = defineProps({
  label: String,
  icon: String,
  toggle: Boolean
});

const toggled = ref(false);

function toggle_() {
  if (props.toggle || toggled.value) {
    toggled.value = !toggled.value;
  }
}

defineExpose({
  toggled
});
</script>

<template>
  <button class="iwy-button" @click="toggle_()" :class="{ 'toggled': toggled }">
    <IwyIcon v-if="props.icon" v-bind:name="props.icon" />
    <span v-if="props.label">{{ props.label }}</span>
  </button>
</template>

<style scoped>
.iwy-button {
  box-sizing: border-box;
  height: 40px;
  display: inline-flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  gap: 5px;
  box-sizing: border-box;
  border: none;
  outline: none;
  padding: 0px 12px;
  cursor: pointer;
  border-radius: 5px;
}

.iwy-button span {
  font-size: 16px;
  font-weight: bold;
}

.iwy-button {
  border: 2px solid v-bind("theme.colFg");
  background-color: v-bind("theme.colBg");
  color: v-bind("theme.colFg");
}

.iwy-button:active, .iwy-button.toggled {
  background-color: v-bind("theme.colFg");
  color: v-bind("theme.colBg");
}

.iwy-button svg {
  fill: v-bind("theme.colFg");
}

.iwy-button:active svg, .iwy-button.toggled svg {
  fill: v-bind("theme.colBg");
}
</style>
