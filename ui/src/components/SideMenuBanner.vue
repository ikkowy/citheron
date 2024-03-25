<script setup>
import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

const props = defineProps({
  caption: String,
  buttonLeftEnabled: {
    type: Boolean,
    default: true
  },
  buttonRightEnabled: {
    type: Boolean,
    default: true
  },
  buttonLeftActive: {
    type: Boolean,
    default: true
  },
  buttonRightActive: {
    type: Boolean,
    default: true
  },
  buttonLeftIcon: String,
  buttonRightIcon: String,
  buttonLeftAction: {
    type: Function,
    default: () => { }
  },
  buttonRightAction: {
    type: Function,
    default: () => { }
  }
});
</script>

<template>
  <div class="side-menu-banner" v-if="props.caption || props.buttonLeftEnabled || props.buttonRightEnabled">
    <a v-if="props.buttonLeftEnabled && props.buttonLeftIcon"
       @click="props.buttonLeftAction()"
       :class="{ 'side-menu-banner-button': true, 'left': true, 'active': props.buttonLeftActive }">
      <iwy-icon :name="props.buttonLeftIcon" :fill="theme.colFg" />
    </a>
    <a v-if="props.buttonRightEnabled && props.buttonRightIcon"
       @click="props.buttonRightAction()"
       :class="{ 'side-menu-banner-button': true, 'right': true, 'active': props.buttonRightActive }">
      <iwy-icon :name="props.buttonRightIcon" :fill="theme.colFg" />
    </a>
    <span v-if="props.caption">{{ props.caption }}</span>
  </div>
</template>

<style scoped>
.side-menu-banner {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 40px;
  font-weight: bold;
  color: v-bind("theme.colFg");
  user-select: none;
}

.side-menu-banner span {
  padding: 6px 8px;
  background-color: v-bind("theme.colFg");
  color: v-bind("theme.colBg");
  border-radius: 7px;
  height: 1em;
}

.side-menu-banner-button {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 40px;
  height: 40px;
  cursor: pointer;
}

.side-menu-banner-button svg {
  fill: v-bind("theme.colFg");
}

.side-menu-banner-button:not(.active) svg {
  fill: gray;
  cursor: not-allowed;
}

.side-menu-banner-button.active:hover {
  background-color: v-bind("theme.colFg");
}

.side-menu-banner-button.active:hover svg {
  fill: v-bind("theme.colBg");
}

.side-menu-banner-button.left {
  left: 0;
}

.side-menu-banner-button.right {
  right: 0;
}
</style>
