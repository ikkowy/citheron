<script setup>
</script>

<template>
  <button class="click-button">
    <slot />
  </button>
</template>

<style scoped>
.click-button {
  box-sizing: border-box;
  border: none;
  outline: none;
  font-size: 16px;
  padding: 7px 15px;
  border-radius: 5px;
  font-weight: bold;
}

.click-button:hover {
    cursor: pointer;
}
</style>
