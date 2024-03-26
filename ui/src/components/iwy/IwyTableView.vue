<script setup>
import { ref } from "vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

const props = defineProps({
  lineNumbers: Boolean,
  highlightHoveredLine: Boolean,
  selectableLines: Boolean
});

const table = ref(null);
const header = ref(null);

const columns = ref([]);
const records = ref([]);

function addColumn(column, title=null) {
  if (title === null)
    title = column;

  if (!column.match(/^[_a-zA-Z][_a-zA-Z0-9]*$/))
    throw "invalid column name";

  if (columns.value.includes(column))
    throw "column name already used";

  columns.value.push(column);
}

// function changeColumnTitle(column, title) {
// }

function addRow(record) {
  records.value.push(record);
}

defineExpose({
  addColumn,
  addRow
});
</script>

<template>
  <table class="iwy-table-view" ref="table">
    <tr ref="header">
      <th v-if="props.selectableLines"></th>
      <th v-if="props.lineNumbers" style="text-align: center">#</th>
      <th v-for="column in columns" :key="column">{{ column }}</th>
    </tr>
    <tr v-for="(record, index) in records" :key="index">
      <td v-if="props.selectableLines"><input type="checkbox"></td>
      <td v-if="props.lineNumbers" style="text-align: right">{{ index + 1 }}</td>
      <td v-for="column in columns" :key="column">{{ record[column] }}</td>
    </tr>
  </table>
</template>

<style scoped>
.iwy-table-view {
  width: 100%;
}

table, th, td {
  border-collapse: collapse;
  border: 2px solid v-bind("theme.colFg");
}

th, td {
  padding: 5px 10px;
}

th {
  text-align: left;
}

tr:not(:first-child):hover {
  background-color: v-bind("props.highlightHoveredLine ? 'red' : 'initial'");
}
</style>
