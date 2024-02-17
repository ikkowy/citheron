<script setup>
import { computed, provide } from "vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

const props = defineProps({
  width: String,
  height: String,
  top: String,
  position: {
    type: String,
    default: "left",
    validator(value) {
      return ["left", "right"].includes(value);
    }
  },
  entryDash: {
    type: String,
    default: "none",
    validator(value) {
      return ["none", "left", "right"].includes(value);
    }
  },
  open: {
    type: Boolean,
    default: true
  }
});

provide("entryDash", props.entryDash);

const right = computed(() => {
  return props.position === "right" ? "0px" : "initial";
});
</script>

<template>
  <aside class="side-menu">
    <slot />
  </aside>
</template>

<style scoped>
.side-menu {
  box-sizing: border-box;
  position: absolute;
  overflow: scroll;
  top: v-bind("props.top");
  right: v-bind(right);
  width: v-bind("props.open ? props.width : '0px'");
  height: v-bind("props.height");
  background-color: v-bind("theme.colBg1");
}
</style>
