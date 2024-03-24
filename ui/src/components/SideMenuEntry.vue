<script setup>
import { inject } from "vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

const props = defineProps({
  label: String,
  icon: String
});

const entryDash = inject("entryDash");
</script>

<template>
  <div class="side-menu-entry" v-bind:class="`side-menu-entry-dash-${entryDash}`">
    <IwyIcon v-if="props.icon" v-bind:name="props.icon" v-bind:fill="theme.colFg" />
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
  background-color: v-bind("theme.colBg");
  color: v-bind("theme.colFg");
  user-select: none;
}

.side-menu-entry:hover {
  cursor: pointer;
  background-color: v-bind("theme.colFg");
  color: v-bind("theme.colBg");
}

.side-menu-entry svg {
  fill: v-bind("theme.colFg");
}

.side-menu-entry:hover svg {
  fill: v-bind("theme.colBg");
}

.side-menu-entry span {
  margin-left: 10px;
  font-weight: bold;
  height: 1em;
}
</style>
