<script setup>
import { defineProps, inject } from "vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

import IconElement from "./IconElement.vue";

const props = defineProps({
  label: String,
  icon: String
});

const entryDash = inject("entryDash");
</script>

<template>
  <div class="side-menu-entry" v-bind:class="`side-menu-entry-dash-${entryDash}`">
    <IconElement v-if="props.icon" v-bind:name="props.icon" v-bind:fill="theme.colFg2" />
    <span>{{ props.label }}</span>
  </div>
</template>

<style scoped>
.side-menu-entry {
  box-sizing: border-box;
  display: flex;
  align-items: center;
  width: 100%;
  height: 40px;
  padding-left: 20px;
  padding-right: 20px;
  border-left: none;
  border-right: none;
  background-color: v-bind("theme.colBg2");
  color: v-bind("theme.colFg2");
  user-select: none;
}

.side-menu-entry:hover {
  cursor: pointer;
  background-color: v-bind("theme.colBg3");
}

.side-menu-entry span {
  margin-left: 10px;
  font-weight: bold;
}

.side-menu-entry-dash-left:hover {
  padding-left: 15px;
  border-left: 5px solid v-bind("theme.colFg2");
}

.side-menu-entry-dash-right:hover {
  padding-right: 15px;
  border-right: 5px solid v-bind("theme.colFg2");
}
</style>
