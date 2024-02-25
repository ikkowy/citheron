<script setup>
import { ref } from "vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

const props = defineProps({
  width: String,
  placeholder: String,
  icon: String,
  password: Boolean,
  invalid: Boolean,
  button: String
});

const showPassword = ref(false);
const focus = ref(false);
</script>

<template>
  <div class="text-field" v-bind:width="props.width">
    <div class="text-field-inner">
      <iwy-icon v-if="props.icon" v-bind:fill="props.invalid ? theme.colRed : theme.colFg1" v-bind:name="props.icon" />
      <input class="text-field-input" v-bind:type="props.password && !showPassword ? 'password' : 'text'" v-bind:placeholder="props.placeholder" v-on:focusin="focus = true" v-on:focusout="focus = false">
      <iwy-icon class="text-field-show-password" v-bind:fill="props.invalid ? theme.colRed : theme.colFg1" v-bind:name="showPassword ? 'VisibilityOff' : 'Visibility'" v-if="props.password" v-on:click="showPassword = !showPassword" />
    </div>
    <button class="text-field-button" v-if="props.button">{{ props.button }}</button>
  </div>
</template>

<style scoped>
.text-field {
  display: inline-flex;
}

.text-field-inner {
  display: inline-flex;
  position: relative;
  flex-direction: row;
  gap: 10px;
  width: 100%;
  padding: 6px 12px;
  border: 2px solid v-bind("props.invalid ? theme.colRed : theme.colFg1");
  border-right: v-bind("props.button ? 'none' : `2px solid ${props.invalid ? theme.colRed : theme.colFg1}`");
  border-radius: 5px;
  border-top-right-radius: v-bind("props.button ? '0' : '5px'");
  border-bottom-right-radius: v-bind("props.button ? '0' : '5px'");
}

.text-field-input {
  width: 100%;
  margin: 0;
  padding: 0;
  border: none;
  outline: none;
  font-size: 16px;
  background-color: transparent;
  color: v-bind("props.invalid ? theme.colRed : theme.colFg1");
}

.text-field-input::placeholder {
  opacity: 0.7;
}

.text-field-input::selection {
  background-color: v-bind("theme.colFg1");
  color: v-bind("theme.colBg1");
}

.text-field-show-password:hover {
  cursor: pointer;
}

.text-field button {
  padding-left: 10px;
  padding-right: 10px;
  border: none;
  border-top-right-radius: 5px;
  border-bottom-right-radius: 5px;
  font-weight: bold;
  border: 2px solid v-bind("props.invalid ? theme.colRed : theme.colFg1");
  background-color: v-bind("props.invalid ? theme.colRed : theme.colFg1");
  color: v-bind("props.invalid ? theme.colLight1 : theme.colBg1");
  cursor: pointer;
}

.text-field button:active {
  background-color: v-bind("theme.colBg1");
  color: v-bind("props.invalid ? theme.colRed : theme.colFg1");
}
</style>
