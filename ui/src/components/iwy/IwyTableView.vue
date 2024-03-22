<script setup>
import { ref } from "vue";

const props = defineProps({
  lineNumbers: Boolean
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

function changeColumnTitle(column, title) {
}

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
      <th v-for="column in columns">{{ column }}</th>
    </tr>
    <tr v-for="record in records">
      <td v-for="column in columns">{{ record[column] }}</td>
    </tr>
  </table>
</template>

<style scoped>
.iwy-table-view {
  width: 100%;
}

table, th, td {
  border-collapse: collapse;
  border: 2px solid;
}

th, td {
  padding: 5px 10px;
}

th {
  text-align: left;
}
</style>
