<template>
    <div>
      <Navbar />
      <Nuxt />
      <Footer />
    </div>
  </template>
  
  
  <script>
  import Navbar from "~/components/Navbar";
  import Footer from "~/components/Footer";
  import Comments from "@/components/Comments";
  
  export default {
    components: {
      Footer,
      Navbar,
      Comments,
    }
  };
  </script>
  
  <style>
  
  </style>