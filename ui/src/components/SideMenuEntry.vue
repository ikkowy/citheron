<script setup>
import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

const props = defineProps({
  label: String,
  icon: String
});
</script>

<template>
  <div class="side-menu-entry">
    <IwyIcon v-if="props.icon" :name="props.icon" :fill="theme.colFg" />
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
