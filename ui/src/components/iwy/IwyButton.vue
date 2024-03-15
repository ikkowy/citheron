<script setup>
import { ref } from "vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

const props = defineProps({
  label: String,
  icon: String
});

const toggled = ref(false);
</script>

<template>
  <button class="iwy-button">
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
  height: 16px;
  font-size: 16px;
  font-weight: bold;
}

.iwy-button {
  border: 2px solid v-bind("theme.colFg1");
  background-color: v-bind("theme.colFg1");
  color: v-bind("theme.colBg1");
}

.iwy-button:active {
  background-color: v-bind("theme.colBg1");
  color: v-bind("theme.colFg1");
}

.iwy-button svg {
  fill: v-bind("theme.colBg1");
}

.iwy-button:active svg {
  fill: v-bind("theme.colFg1");
}
</style>
