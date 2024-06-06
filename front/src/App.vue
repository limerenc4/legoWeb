<script >
export default{
  data(){
    return{
      num:0,
      uname:"张三",
      id:"name",
      message:"消息"
    }
  },
  computed:{
    reserveUname:function(){
      return this.uname.split('').reverse().join('')
    }
  },
  methods:{
    changeUname(){
      this.uname = "李四"
    },
    changeId(){
      this.id = 'test'
    },
  },
}
</script>

<template>
  <header>
    <p>{{ num }}</p>
    <p>{{ uname }}</p>
    <p v-once>{{ uname }}</p>
    <button @click="changeUname"> changeUname </button>
    <p v-bind:id="id"> v-bind</p>
    <button @click="changeId"> changeID </button>
    <p>{{ reserveUname }}</p>
  </header>

  <main>
    <TheWelcome />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
