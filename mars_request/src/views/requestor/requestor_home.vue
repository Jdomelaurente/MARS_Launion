<template>
  <div class="min-h-screen font-sans">
    <!-- Navbar -->
    <nav class="flex flex-col md:flex-row justify-between items-center py-4 px-6 md:px-12 bg-white border-b shadow-sm gap-4 md:gap-0">
      <div class="flex items-center gap-2.5">
        <img :src="logoImg" alt="Logo" class="w-10 h-10 object-contain" />
        <div class="flex flex-col">
          <span class="font-bold text-slate-800 text-sm leading-tight">StandAlone</span>
          <span class="text-[0.65rem] text-slate-500 font-medium whitespace-nowrap">La Union Senior High School</span>
        </div>
      </div>
      <div class="flex flex-wrap justify-center items-center gap-4 md:gap-12 text-[0.8rem] md:text-[0.95rem]">
        <router-link to="/requestor/home" class="text-cyan-500 font-bold">Home</router-link>
        <a href="#" class="text-slate-800 font-bold hover:text-cyan-500 transition-colors">Navigation</a>
        <a href="#" class="text-slate-800 font-bold hover:text-cyan-500 transition-colors">Navigation</a>
        <a href="#" class="text-slate-800 font-bold hover:text-cyan-500 transition-colors">Navigation</a>
        <button @click="openCheckModal" class="px-4 md:px-6 py-2 rounded font-bold text-white bg-[#154252] hover:bg-[#0d2a35] transition-colors whitespace-nowrap">
          Check Your Request
        </button>
      </div>
    </nav>

    <!-- Hero Section -->
    <div class="relative min-h-[450px] md:min-h-[500px] flex flex-col justify-center bg-[#154252] bg-cover bg-center bg-blend-overlay px-6 md:px-12 lg:px-24 py-16 md:py-0 text-center md:text-left"
         :style="{ backgroundImage: `linear-gradient(rgba(21, 66, 82, 0.7), rgba(21, 66, 82, 0.7)), url(${bgImg})` }">

      <div class="max-w-4xl relative z-10 mx-auto md:mx-0">
        <p class="text-slate-300 md:text-slate-200 font-bold mb-2 text-sm md:text-base">La Union Senior High School, Cabadbaran City</p>
        <h1 class="text-white text-3xl sm:text-4xl md:text-5xl lg:text-5xl font-extrabold mb-6 leading-tight">
          Request your School Document <span class="text-yellow-400">Online!</span>
        </h1>
        <p class="text-slate-300 md:text-slate-200 max-w-2xl mb-10 leading-relaxed text-sm md:text-base mx-auto md:mx-0">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
          Ut enim ad minim veniam, quis nostrud exercitation ullamco
        </p>

        <!-- CTA Button with character -->
        <div class="relative inline-block mt-12 group">
          <div class="absolute -top-12 -right-24 flex items-center gap-2 pointer-events-none z-20">
            <!-- Character sitting -->
            <div class="relative w-12 h-12">
               <img :src="sittingPersonImg" alt="Sitting" class="absolute bottom-0 right-0 w-14 h-14 object-contain" />
            </div>
            <!-- The "HERE!" Bubble -->
            <div class="animate-bounce -mt-4">
               <div class="bg-white px-3 py-1.5 rounded-md text-[0.8rem] md:text-[0.9rem] font-black text-[#154252] shadow-xl border-2 border-[#154252] relative whitespace-nowrap">
                 HERE!
                 <!-- Left pointing tail -->
                 <div class="absolute top-1/2 -left-1.5 w-2.5 h-2.5 bg-white border-l-2 border-b-2 border-[#154252] transform -translate-y-1/2 rotate-45"></div>
               </div>
            </div>
          </div>
          
          <button @click="openModal" class="px-12 py-4 bg-yellow-400 hover:bg-yellow-500 text-slate-900 font-black rounded-sm shadow-xl transition-all transform hover:scale-105 uppercase tracking-wide text-base min-w-[280px]">
            Make a request
          </button>
        </div>
      </div>

      <!-- Decorative circles -->
      <div class="absolute right-12 lg:right-32 top-1/2 -translate-y-1/2 hidden xl:flex gap-8">
        <div class="w-40 h-40 rounded-full bg-white opacity-95"></div>
        <div class="w-40 h-40 rounded-full bg-white opacity-95"></div>
      </div>
    </div>

    <!-- Content Sections -->
    <div class="max-w-7xl mx-auto py-12 md:py-20 px-6 md:px-12 grid grid-cols-1 md:grid-cols-2 gap-12 md:gap-20">
      <div class="flex flex-col gap-12">
        <section>
          <h2 class="text-3xl font-black text-[#154252] mb-6 border-b-4 border-slate-100 pb-2">VISION</h2>
          <p class="text-slate-700 leading-relaxed font-medium">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
          </p>
        </section>

        <section>
          <h2 class="text-3xl font-black text-[#154252] mb-6 border-b-4 border-slate-100 pb-2">MISSION</h2>
          <p class="text-slate-700 leading-relaxed font-medium">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
          </p>
        </section>
      </div>

      <div>
        <h2 class="text-3xl font-black text-[#154252] mb-6 border-b-4 border-slate-100 pb-2">LOREM IPSUM</h2>
        <div class="space-y-8">
          <p class="text-slate-700 leading-relaxed font-medium">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
            Ut enim ad minim veniam.
          </p>
          <p class="text-slate-700 leading-relaxed font-medium">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
          </p>
          <p class="text-slate-700 leading-relaxed font-medium">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
          </p>
        </div>
      </div>
    </div>

    <!-- ===================== CHECK REQUEST MODAL ===================== -->
    <Teleport to="body">
      <div v-if="showCheckModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4">
        <div class="bg-white w-full max-w-lg rounded-xl shadow-2xl border border-slate-300 overflow-hidden">
          <!-- Header -->
          <div class="px-8 pt-8 pb-4 flex items-start justify-between">
            <div>
              <h2 class="text-2xl font-black text-slate-900">Review Request Document</h2>
              <p class="text-slate-500 text-sm mt-1">Enter the given Request Key of the Graduates.</p>
            </div>
            <div class="flex gap-2 flex-shrink-0">
              <div class="w-9 h-9 rounded-full bg-[#99dbce]"></div>
              <div class="w-9 h-9 rounded-full bg-[#99dbce]"></div>
            </div>
          </div>
          <!-- Input Area -->
          <div class="px-8 pb-4">
            <input
              v-model="checkCode"
              @keyup.enter="handleCheckRequest"
              type="text"
              placeholder=""
              class="w-full border border-slate-400 rounded-sm px-4 text-4xl font-mono font-black tracking-widest text-[#154252] focus:outline-none focus:border-[#154252] transition-all uppercase text-center"
              style="height: 130px; display: flex; align-items: center;"
            />
            <div v-if="checkError" class="mt-2 text-sm text-red-500 font-medium">
              {{ checkError }}
            </div>
            <p class="text-slate-700 text-sm mt-3 leading-relaxed">
              <strong>Note:</strong> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua..
            </p>
          </div>
          <!-- Footer Buttons -->
          <div class="px-8 pb-8 flex items-center justify-between gap-4 mt-2">
            <button
              @click="closeCheckModal"
              class="px-10 py-2.5 border-2 border-slate-800 text-slate-800 font-bold rounded hover:bg-slate-50 transition-colors text-sm"
            >Close</button>
            <button
              @click="handleCheckRequest"
              :disabled="checkLoading"
              class="px-10 py-2.5 bg-yellow-400 hover:bg-yellow-500 text-slate-900 font-black rounded shadow transition-colors disabled:opacity-60 text-sm"
            >
              <span v-if="checkLoading">Searching...</span>
              <span v-else>Review</span>
            </button>
          </div>
        </div>
      </div>
    </Teleport>

    <!-- ===================== REQUEST MODAL ===================== -->
    <Teleport to="body">
      <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4">
        <div class="bg-white w-full max-w-4xl rounded-2xl shadow-2xl border border-slate-200 overflow-y-auto max-h-[95vh] flex flex-col">
          
          <!-- Modal Header -->
          <div class="px-10 pt-10 pb-6 border-b border-slate-100">
            <h2 class="text-3xl font-bold text-center text-slate-900 tracking-tight">Fill-up Information</h2>
            <div class="mt-4 flex flex-wrap items-start gap-2 text-sm">
              <span class="font-bold text-slate-800">Instruction:</span>
              <span class="text-slate-500 flex-1">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</span>
            </div>
          </div>

          <!-- Modal Body -->
          <form @submit.prevent="handleSubmit" class="px-10 py-8 flex flex-col gap-6 flex-1">
            <!-- Row 1: Name -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              <div class="flex flex-col gap-1">
                <label class="text-xs font-semibold text-slate-700">First Name <span class="text-red-500">*</span></label>
                <input v-model="form.first_name" type="text" required class="border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-[#154252] focus:ring-1 focus:ring-[#154252]" />
              </div>
              <div class="flex flex-col gap-1">
                <label class="text-xs font-semibold text-slate-700">Middle Name (Optional)</label>
                <input v-model="form.middle_name" type="text" class="border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-[#154252] focus:ring-1 focus:ring-[#154252]" />
              </div>
              <div class="flex flex-col gap-1">
                <label class="text-xs font-semibold text-slate-700">Last Name <span class="text-red-500">*</span></label>
                <input v-model="form.last_name" type="text" required class="border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-[#154252] focus:ring-1 focus:ring-[#154252]" />
              </div>
              <div class="flex flex-col gap-1">
                <label class="text-xs font-semibold text-slate-700">Suffix (Optional)</label>
                <input v-model="form.suffix" type="text" class="border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-[#154252] focus:ring-1 focus:ring-[#154252]" placeholder="Jr., Sr., III..." />
              </div>
            </div>

            <!-- Row 2: School Info -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              <div class="flex flex-col gap-1">
                <label class="text-xs font-semibold text-slate-700">Sex <span class="text-red-500">*</span></label>
                <select v-model="form.sex" required class="border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-[#154252] focus:ring-1 focus:ring-[#154252] bg-white">
                  <option value="" disabled>Select...</option>
                  <option>Male</option>
                  <option>Female</option>
                </select>
              </div>
              <div class="flex flex-col gap-1">
                <label class="text-xs font-semibold text-slate-700">Year Graduated <span class="text-red-500">*</span></label>
                <input v-model="form.year_graduated" type="text" required class="border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-[#154252] focus:ring-1 focus:ring-[#154252]" placeholder="e.g. 2023" />
              </div>
              <div class="flex flex-col gap-1">
                <label class="text-xs font-semibold text-slate-700">Strand <span class="text-red-500">*</span></label>
                <input v-model="form.strand" type="text" required class="border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-[#154252] focus:ring-1 focus:ring-[#154252]" placeholder="e.g. STEM, ABM..." />
              </div>
              <div class="flex flex-col gap-1">
                <label class="text-xs font-semibold text-slate-700">Birthdate <span class="text-red-500">*</span></label>
                <input v-model="form.birthdate" type="date" required class="border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-[#154252] focus:ring-1 focus:ring-[#154252]" />
              </div>
            </div>

            <!-- Row 3: Contact Info -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              <div class="flex flex-col gap-1">
                <label class="text-xs font-semibold text-slate-700">LRN Number (Optional)</label>
                <input v-model="form.lrn_number" type="text" class="border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-[#154252] focus:ring-1 focus:ring-[#154252]" />
              </div>
              <div class="flex flex-col gap-1">
                <label class="text-xs font-semibold text-slate-700">Active Email Address <span class="text-red-500">*</span></label>
                <input v-model="form.email" type="email" required class="border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-[#154252] focus:ring-1 focus:ring-[#154252]" />
              </div>
              <div class="flex flex-col gap-1">
                <label class="text-xs font-semibold text-slate-700">Phone No. <span class="text-red-500">*</span></label>
                <input v-model="form.phone_number" type="text" required class="border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-[#154252] focus:ring-1 focus:ring-[#154252]" />
              </div>
              <div class="flex flex-col gap-1">
                <label class="text-xs font-semibold text-slate-700">Permanent Address <span class="text-red-500">*</span></label>
                <input v-model="form.permanent_address" type="text" required class="border border-slate-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-[#154252] focus:ring-1 focus:ring-[#154252]" />
              </div>
            </div>

            <!-- File Selection -->
            <div class="flex flex-col gap-2">
              <label class="text-sm font-semibold text-slate-800">Request a Files</label>
              <div class="relative">
                <select v-model="fileSelectValue" @change="addFile" class="w-full border border-slate-300 rounded px-4 py-3 text-sm text-slate-500 appearance-none bg-white focus:outline-none focus:border-[#154252] focus:ring-1 focus:ring-[#154252] cursor-pointer">
                  <option value="" disabled>Select a File</option>
                  <option value="Senior High School Diploma">Senior High School Diploma</option>
                  <option value="Form 138">Form 138</option>
                  <option value="Form 137">Form 137</option>
                </select>
                <div class="pointer-events-none absolute inset-y-0 right-4 flex items-center">
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-slate-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
                  </svg>
                </div>
              </div>

              <!-- Selected Files Display -->
              <div class="border border-slate-200 rounded-lg p-4 min-h-[80px]">
                <div class="flex justify-between items-center mb-3">
                  <span class="text-xs text-slate-400 font-medium">Selected File:</span>
                  <button v-if="selectedFiles.length > 0" type="button" @click="removeAllFiles" class="text-xs text-red-500 font-semibold hover:text-red-700 transition-colors">Remove all</button>
                </div>
                <div class="flex flex-wrap gap-2">
                  <span
                    v-for="(file, index) in selectedFiles"
                    :key="index"
                    class="flex items-center gap-2 bg-[#154252] text-white text-xs font-semibold px-4 py-1.5 rounded-full"
                  >
                    {{ file }}
                    <button type="button" @click="removeFile(index)" class="hover:text-yellow-300 transition-colors font-bold text-sm leading-none">✕</button>
                  </span>
                  <span v-if="selectedFiles.length === 0" class="text-xs text-slate-400 italic">No files selected yet.</span>
                </div>
              </div>
              <div v-if="fileError" class="text-red-500 text-xs font-medium">{{ fileError }}</div>
            </div>

            <!-- Error -->
            <div v-if="submitError" class="text-red-500 text-sm text-center bg-red-50 border border-red-200 rounded p-3">{{ submitError }}</div>
          </form>

          <!-- Modal Footer -->
          <div class="px-10 py-6 border-t border-slate-100 flex flex-col sm:flex-row justify-between items-center gap-4">
            <!-- Branding -->
            <div class="flex items-center gap-3">
              <div class="w-9 h-9 rounded-full bg-[#99dbce] flex items-center justify-center">
                <img :src="logoImg" alt="logo" class="w-6 h-6 object-contain" />
              </div>
              <div class="flex flex-col leading-tight">
                <span class="text-sm font-bold text-slate-800 italic">StandAlone</span>
                <span class="text-[0.6rem] text-slate-500">La union Senior High School</span>
              </div>
            </div>
            <div class="flex gap-4 w-full sm:w-auto">
              <button type="button" @click="closeModal" class="flex-1 sm:flex-none px-8 py-2.5 border-2 border-slate-800 text-slate-800 font-bold rounded hover:bg-slate-50 transition-colors">Cancel</button>
              <button type="button" @click="handleSubmit" :disabled="submitting" class="flex-1 sm:flex-none px-8 py-2.5 bg-yellow-400 hover:bg-yellow-500 font-black text-slate-900 rounded shadow-md transition-colors disabled:opacity-70">
                <span v-if="submitting">Submitting...</span>
                <span v-else>Submit Request</span>
              </button>
            </div>
            <!-- Decorative circles -->
            <div class="hidden sm:flex gap-2">
              <div class="w-8 h-8 rounded-full bg-[#99dbce]"></div>
              <div class="w-8 h-8 rounded-full bg-[#99dbce]"></div>
            </div>
          </div>
        </div>
      </div>
    </Teleport>

    <!-- ===================== SUCCESS MODAL ===================== -->
    <Teleport to="body">
      <div v-if="showSuccess" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4">
        <div class="bg-white w-full max-w-sm rounded-2xl shadow-2xl border border-slate-200 px-10 py-10 text-center">
          <!-- Green Check Icon -->
          <div class="flex justify-center mb-4">
            <div class="w-16 h-16 rounded-full bg-green-500 flex items-center justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-9 h-9 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3">
                <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
              </svg>
            </div>
          </div>
          <h2 class="text-2xl font-black text-green-600 mb-1">Request Sent!</h2>
          <p class="text-sm text-slate-400 mb-4">Your file request has been successfully submitted.</p>
          
          <div class="mb-6 bg-slate-50 border-2 border-dashed border-[#154252] rounded-lg p-4">
            <p class="text-xs text-slate-500 font-bold uppercase tracking-widest mb-1">Your Request Code</p>
            <p class="text-2xl font-black text-[#154252] tracking-wider font-mono">{{ requestCode }}</p>
          </div>

          <div class="text-left mb-6">
            <p class="text-[#e07b2a] font-bold mb-1">Reminder:</p>
            <p class="text-slate-800 text-sm leading-relaxed text-center">Please save your request code. A notification has also been sent to your email address.</p>
          </div>
          <button @click="closeSuccess" class="w-full py-3 bg-[#154252] hover:bg-[#0d2a35] text-white font-bold rounded-lg transition-colors">Close</button>
        </div>
      </div>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';
import bgImg from '@/assets/launion.png';
import logoImg from '@/assets/logo-launion.png';
import sittingPersonImg from '@/assets/sitting_person.png';
import { requestService } from '@/services/api';

const router = useRouter();

// Check Request Modal State
const showCheckModal = ref(false);
const checkCode = ref('');
const checkError = ref('');
const checkLoading = ref(false);

function openCheckModal() {
  showCheckModal.value = true;
  checkCode.value = '';
  checkError.value = '';
}

function closeCheckModal() {
  showCheckModal.value = false;
}

async function handleCheckRequest() {
  if (!checkCode.value.trim()) {
    checkError.value = 'Please enter your request code.';
    return;
  }
  checkLoading.value = true;
  checkError.value = '';
  try {
    await requestService.lookupRequest(checkCode.value.trim());
    closeCheckModal();
    router.push({ name: 'request-details', params: { code: checkCode.value.trim().toUpperCase() } });
  } catch (err) {
    checkError.value = err.response?.data?.error || 'Invalid code. Please try again.';
  } finally {
    checkLoading.value = false;
  }
}

// Modal State
const showModal = ref(false);
const showSuccess = ref(false);
const submitting = ref(false);
const submitError = ref('');
const fileError = ref('');
const fileSelectValue = ref('');
const selectedFiles = ref([]);
const requestCode = ref('');

// Form Data
const form = reactive({
  first_name: '',
  middle_name: '',
  last_name: '',
  suffix: '',
  sex: '',
  year_graduated: '',
  strand: '',
  birthdate: '',
  lrn_number: '',
  email: '',
  phone_number: '',
  permanent_address: '',
});

function openModal() {
  showModal.value = true;
}

function closeModal() {
  showModal.value = false;
  resetForm();
}

function closeSuccess() {
  showSuccess.value = false;
}

function addFile() {
  const val = fileSelectValue.value;
  if (!val) return;
  if (!selectedFiles.value.includes(val)) {
    selectedFiles.value.push(val);
  }
  // Reset the dropdown so it can be selected again for another file
  fileSelectValue.value = '';
}

function removeFile(index) {
  selectedFiles.value.splice(index, 1);
}

function removeAllFiles() {
  selectedFiles.value = [];
}

function resetForm() {
  Object.keys(form).forEach(k => { form[k] = ''; });
  selectedFiles.value = [];
  fileSelectValue.value = '';
  submitError.value = '';
  fileError.value = '';
}

async function handleSubmit() {
  fileError.value = '';
  submitError.value = '';

  if (selectedFiles.value.length === 0) {
    fileError.value = 'Please select at least one file to request.';
    return;
  }

  submitting.value = true;
  try {
    const response = await requestService.submitRequest({
      ...form,
      requested_files: selectedFiles.value,
    });
    requestCode.value = response.data?.request_code;
    if (requestCode.value) {
      router.push({ name: 'request-details', params: { code: requestCode.value } });
    } else {
      submitError.value = 'Request was successful but no code was returned.';
    }

  } catch (err) {
    const data = err.response?.data;
    if (data && typeof data === 'object' && !Array.isArray(data)) {
      const firstKey = Object.keys(data)[0];
      submitError.value = Array.isArray(data[firstKey]) ? data[firstKey][0] : data[firstKey];
    } else if (typeof data === 'string') {
      submitError.value = 'An error occurred on the server. Please try again later.';
    } else {
      submitError.value = 'Something went wrong. Please try again.';
    }
  } finally {
    submitting.value = false;
  }
}
</script>

<style scoped>
/* Any custom styling if needed */
</style>
