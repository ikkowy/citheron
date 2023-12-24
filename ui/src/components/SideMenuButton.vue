<template>

    <div class="side-menu-button">
        <span>{{ props.text }}</span>
    </div>

</template>

<script setup>
import { defineProps } from "vue";

const props = defineProps(["text"]);
</script>

<style scoped>
.side-menu-button {
    display: flex;
    align-items: center;
    width: 100%;
    height: 40px;
    color: #d9d9d9;
    user-select: none;
}

.side-menu-button:hover {
    cursor: pointer;
    background-color: #262626;
}

.side-menu-button span {
    margin-left: 30px;
}
</style>
