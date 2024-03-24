<script setup>
import { computed, provide } from "vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

const props = defineProps({
  // width: String,
  // height: String,
  // top: String,
  // position: {
  //   type: String,
  //   default: "left",
  //   validator(value) {
  //     return ["left", "right"].includes(value);
  //   }
  // },
  open: {
    type: Boolean,
    default: true
  }
});
</script>

<template>
  <aside class="side-menu">
    <slot />
  </aside>
</template>

<style scoped>
.side-menu {
  display: v-bind("props.open ? 'initial' : 'none'");
  box-sizing: border-box;
  /* width: v-bind("props.width"); */
  /* height: v-bind("props.height"); */
  background-color: v-bind("theme.colBg");
}
</style>
