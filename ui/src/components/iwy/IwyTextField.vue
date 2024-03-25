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
  <div class="iwy-text-field" v-bind:width="props.width">
    <div class="iwy-text-field-inner">
      <IwyIcon
          v-if="props.icon"
          :fill="props.invalid ? theme.colRed : theme.colFg"
          :name="props.icon" />
      <input
          class="iwy-text-field-input"
          :type="props.password && !showPassword ? 'password' : 'text'"
          :placeholder="props.placeholder"
          @focusin="focus = true"
          @focusout="focus = false">
      <IwyIcon
          class="iwy-text-field-show-password"
          :fill="props.invalid ? theme.colRed : theme.colFg"
          :name="showPassword ? 'eye-off' : 'eye'"
          v-if="props.password"
          @click="showPassword = !showPassword" />
    </div>
    <button class="iwy-text-field-button" v-if="props.button">{{ props.button }}</button>
  </div>
</template>

<style scoped>
.iwy-text-field {
  display: inline-flex;
  height: 40px;
}

.iwy-text-field-inner {
  display: inline-flex;
  position: relative;
  flex-direction: row;
  align-items: center;
  gap: 10px;
  width: 100%;
  padding: 6px 12px;
  border: 2px solid v-bind("props.invalid ? theme.colRed : theme.colFg");
  border-right: v-bind("props.button ? 'none' : `2px solid ${props.invalid ? theme.colRed : theme.colFg}`");
  border-radius: 5px;
  border-top-right-radius: v-bind("props.button ? '0' : '5px'");
  border-bottom-right-radius: v-bind("props.button ? '0' : '5px'");
}

.iwy-text-field-input {
  width: 100%;
  margin: 0;
  padding: 0;
  border: none;
  outline: none;
  font-size: 16px;
  background-color: transparent;
  color: v-bind("props.invalid ? theme.colRed : theme.colFg");
}

.iwy-text-field-input::placeholder {
  opacity: 1;
  font-style: italic;
}

.iwy-text-field-input:focus::placeholder {
  color: transparent;
}

.iwy-text-field-input::selection {
  background-color: v-bind("theme.colFg");
  color: v-bind("theme.colBg");
}

.iwy-text-field-show-password:hover {
  cursor: pointer;
}

.iwy-text-field-button {
  padding-left: 10px;
  padding-right: 10px;
  border: none;
  border-top-right-radius: 5px;
  border-bottom-right-radius: 5px;
  font-size: 16px;
  font-weight: bold;
  border: 2px solid v-bind("props.invalid ? theme.colRed : theme.colFg");
  background-color: v-bind("props.invalid ? theme.colRed : theme.colFg");
  color: v-bind("props.invalid ? theme.colLight1 : theme.colBg");
  cursor: pointer;
}

.iwy-text-field button:active {
  background-color: v-bind("theme.colBg");
  color: v-bind("props.invalid ? theme.colRed : theme.colFg");
}
</style>
