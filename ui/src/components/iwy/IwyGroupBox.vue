<script setup>
import { ref } from "vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

const props = defineProps({
  title: String,
  minimizable: {
    type: Boolean,
    default: false
  },
  minimized: {
    type: Boolean,
    default: false
  }
});

const minimized = ref(props.minimized);
</script>

<template>
  <section class="iwy-group-box">
    <span class="iwy-group-box-header"
          style="display: flex; gap: 5px">
      <IwyIcon v-if="minimizable || minimized" :name="minimized ? 'chevron-down' : 'chevron-up'"
               @click="minimized = !minimized"
               style="cursor: pointer" />
      <span class="iwy-group-box-title">{{ props.title }}</span>
    </span>
    <slot v-if="!minimized"></slot>
  </section>
</template>

<style scoped>
.iwy-group-box {
  box-sizing: border-box;
  position: relative;
  padding: 12px 10px 5px 10px;
  border: 2px solid v-bind("theme.colFg");
  border-radius: 5px;
}

.iwy-group-box-header {
  position: absolute;
  top: -0.8em;
  left: 10px;
  padding: 0 7px;
  background-color: v-bind("theme.colBg");
  user-select: none;
}

.iwy-group-box-header span {
  font-weight: bold;
}

.iwy-group-box-header svg {
  fill: v-bind("theme.colFg");
}
</style>
