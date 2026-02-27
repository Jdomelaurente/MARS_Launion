<template>
  <div class="flex flex-col gap-10">
    <div class="flex flex-col gap-2">
      <h1 class="text-2xl md:text-3xl font-extrabold text-[#333] tracking-tight">Admin Dashboard</h1>
      <p class="text-slate-500 text-sm">Overview of system performance and record requests.</p>
    </div>

    <!-- Stat Cards -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-4">
      <div v-for="card in statCards" :key="card.label" 
           class="bg-white p-6 rounded-lg border border-slate-200 shadow-sm flex flex-col gap-2 relative overflow-hidden group hover:shadow-md transition-shadow">
        <div class="absolute top-0 right-0 w-24 h-24 -mr-8 -mt-8 opacity-5 transition-transform group-hover:scale-110" :style="{ color: card.color }">
          <component :is="card.icon" class="w-full h-full" />
        </div>
        <span class="text-xs font-bold text-slate-500 uppercase tracking-widest">{{ card.label }}</span>
        <div class="flex items-end gap-2">
          <span class="text-3xl font-black text-[#00334d]">{{ card.value }}</span>
        </div>
        <div class="w-full h-1 mt-2 rounded-full bg-slate-100 overflow-hidden">
          <div class="h-full rounded-full transition-all duration-1000" :style="{ width: '100%', backgroundColor: card.color }"></div>
        </div>
      </div>
    </div>

    <!-- Bottom Row -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <!-- Strand Breakdown -->
      <div class="bg-white rounded-lg shadow-sm border border-slate-200 overflow-hidden flex flex-col">
        <div class="px-6 py-4 bg-slate-50 border-b flex justify-between items-center">
          <h3 class="font-bold text-[#00334d] text-sm uppercase tracking-wide">Requests by Strand</h3>
        </div>
        <div v-if="loadingStats" class="p-12 text-center text-slate-400">Loading statistics...</div>
        <div v-else class="overflow-x-auto flex-grow">
          <table class="w-full text-left text-sm">
            <thead>
              <tr class="bg-slate-50 border-b font-bold text-slate-600 uppercase text-[0.65rem] tracking-wider">
                <th class="px-6 py-3">Strand</th>
                <th class="px-6 py-3 text-center">Count</th>
                <th class="px-6 py-3">Distribution</th>
              </tr>
            </thead>
            <tbody class="divide-y">
              <tr v-for="row in stats.strand_breakdown" :key="row.strand_name" class="hover:bg-slate-50">
                <td class="px-6 py-4 font-bold text-slate-800">{{ row.strand_name || 'Not Specified' }}</td>
                <td class="px-6 py-4 text-center font-bold">{{ row.count }}</td>
                <td class="px-6 py-4">
                  <div class="flex items-center gap-3">
                    <div class="flex-1 h-2 bg-slate-100 rounded-full overflow-hidden">
                      <div class="h-full bg-[#ffca28] rounded-full" :style="{ width: strandPercent(row.count) + '%' }"></div>
                    </div>
                    <span class="text-[0.65rem] font-black text-slate-500 w-8 text-right">{{ strandPercent(row.count) }}%</span>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Upcoming Pickup Slots -->
      <div class="bg-white rounded-lg shadow-sm border border-slate-200 overflow-hidden flex flex-col">
        <div class="px-6 py-4 bg-slate-50 border-b flex justify-between items-center">
          <h3 class="font-bold text-[#00334d] text-sm uppercase tracking-wide">Upcoming Pickups</h3>
          <button @click="$emit('change-view', 'pickup_scheduling')" class="text-[0.7rem] font-bold text-cyan-600 hover:underline px-2">Manage</button>
        </div>
        <div v-if="loadingStats" class="p-12 text-center text-slate-400">Loading schedule...</div>
        <div v-else-if="!stats.upcoming_slots?.length" class="p-12 text-center text-slate-400 italic text-sm">No upcoming slots scheduled.</div>
        <div v-else class="divide-y flex-grow">
          <div v-for="slot in stats.upcoming_slots" :key="slot.id" class="px-6 py-5 hover:bg-slate-50 transition-colors">
            <div class="flex justify-between items-start mb-2">
               <span class="font-bold text-[#00334d] text-sm">{{ formatDateFull(slot.date) }}</span>
               <span class="text-[0.65rem] font-black text-slate-500">{{ slot.booked_slots }} / {{ slot.max_slots }}</span>
            </div>
            <div class="w-full h-1.5 bg-slate-100 rounded-full overflow-hidden">
              <div class="h-full bg-amber-400 rounded-full transition-all duration-1000" :style="{ width: (Math.min((slot.booked_slots/slot.max_slots)*100, 100)) + '%' }"></div>
            </div>
          </div>
        </div>
        <div class="p-4 bg-amber-50 border-t mt-auto">
           <p class="text-[0.6rem] text-amber-700 font-bold text-center leading-tight">Note: Inform students to arrive 15 minutes before their chosen slot.</p>
        </div>
      </div>

      <!-- Popular Documents -->
      <div class="bg-white rounded-lg shadow-sm border border-slate-200 overflow-hidden flex flex-col">
        <div class="px-6 py-4 bg-slate-50 border-b flex justify-between items-center">
          <h3 class="font-bold text-[#00334d] text-sm uppercase tracking-wide">Document Popularity</h3>
          <button @click="$emit('change-view', 'document_types')" class="text-[0.7rem] font-bold text-cyan-600 hover:underline px-2">Manage Types</button>
        </div>
        <div v-if="loadingStats" class="p-12 text-center text-slate-400">Loading document stats...</div>
        <div v-else class="overflow-x-auto flex-grow">
          <table class="w-full text-left text-sm">
            <thead>
              <tr class="bg-slate-50 border-b font-bold text-slate-600 uppercase text-[0.65rem] tracking-wider">
                <th class="px-6 py-3">Document</th>
                <th class="px-6 py-3 text-center">Requests</th>
                <th class="px-6 py-3">Revenue Est.</th>
              </tr>
            </thead>
            <tbody class="divide-y">
              <tr v-for="doc in stats.doc_breakdown" :key="doc.document" class="hover:bg-slate-50">
                <td class="px-6 py-3 font-bold text-slate-800 text-xs">{{ doc.document }}</td>
                <td class="px-6 py-3 text-center font-bold">{{ doc.count }}</td>
                <td class="px-6 py-3 text-right pr-6 font-mono text-xs text-green-600 font-bold">
                  \u20b1{{ (doc.count * (doc.price || 0)).toLocaleString() }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="p-3 bg-slate-50 border-t mt-auto">
           <p class="text-[0.6rem] text-slate-500 font-bold text-center">Total Estimated Revenue: <span class="text-green-600">\u20b1{{ stats.doc_breakdown?.reduce((acc, d) => acc + (d.count * d.price), 0).toLocaleString() }}</span></p>
        </div>
      </div>

      <!-- Recent Requests -->
      <div class="bg-white rounded-lg shadow-sm border border-slate-200 overflow-hidden flex flex-col">
        <div class="px-6 py-4 bg-slate-50 border-b flex justify-between items-center">
          <h3 class="font-bold text-[#00334d] text-sm uppercase tracking-wide">Recent Submissions</h3>
          <button @click="$emit('change-view', 'record_requests')" class="text-[0.7rem] font-bold text-cyan-600 hover:underline px-2">View All</button>
        </div>
        <div v-if="loadingStats" class="p-12 text-center text-slate-400">Loading requests...</div>
        <div v-else class="divide-y flex-grow">
          <div v-for="req in stats.recent_requests" :key="req.id" 
               @click="$emit('open-modal', req)"
               class="px-6 py-4 flex items-center justify-between hover:bg-slate-50 cursor-pointer transition-colors group">
            <div class="flex items-center gap-4">
              <div class="w-10 h-10 rounded-full bg-[#154252] text-white flex items-center justify-center font-bold text-xs ring-2 ring-slate-100">
                {{ initials(req.first_name, req.last_name) }}
              </div>
              <div class="flex flex-col">
                <div class="flex items-center gap-2">
                  <span class="font-bold text-sm text-[#00334d] group-hover:text-cyan-600 transition-colors">{{ req.first_name }} {{ req.last_name }}</span>
                  <component :is="AttachmentIcon" v-if="req.documents?.length > 0" class="w-3.5 h-3.5 text-amber-500" />
                </div>
                <span class="text-[0.7rem] text-slate-500 font-medium">{{ req.strand_display || req.strand || 'No Strand' }} \u00b7 {{ formatDate(req.submitted_at) }}</span>
              </div>
            </div>
            <span class="px-3 py-1 rounded-full text-[0.65rem] font-bold uppercase tracking-wider" :class="statusClass(req.status)">
              {{ req.status }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { Paperclip as AttachmentIcon } from 'lucide-vue-next';

defineProps({
  stats: Object,
  statCards: Array,
  loadingStats: Boolean,
  strandPercent: Function,
  formatDate: Function,
  formatDateFull: Function,
  initials: Function,
  statusClass: Function
});

defineEmits(['change-view', 'open-modal']);
</script>
