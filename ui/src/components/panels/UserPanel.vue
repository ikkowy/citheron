<script setup>
import DashboardPanel from '../DashboardPanel.vue';
import IwyButton from '../iwy/IwyButton.vue';

import { useAppStore } from "@/storages/useAppStore";
import IwyTextField from '../iwy/IwyTextField.vue';
const appStore = useAppStore();
const { theme } = appStore;
</script>

<template>
  <DashboardPanel>
    <div style="display: flex; flex-direction: column; gap: 10px">
      <div style="display: flex; flex-direction: row; gap: 10px">
        <IwyTextField icon="search" button="Search" />
        <IwyButton icon="filter" label="Filter" />
        <IwyButton icon="plus" label="Create" />
        <IwyButton icon="minus" label="Remove" />
        <IwyButton icon="export" label="Export" />
      </div>
      <table>
        <tr>
          <th></th>
          <th>Username</th>
          <th>E-Mail</th>
          <th>Created</th>
          <th>Enabled</th>
        </tr>
        <tr>
          <td><input type="checkbox"></td>
          <td>vincent</td>
          <td>vincent@example.com</td>
          <td>2024-03-15</td>
          <td>true</td>
        </tr>
      </table>
    </div>
  </DashboardPanel>
</template>

<style scoped>
table, th, td {
  border-collapse: collapse;
}

th, td {
  padding: 5px 10px;
  border: 2px solid v-bind("theme.colFg1");
}

th {
  text-align: left;
}
</style>
