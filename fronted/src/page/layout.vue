<template>
  <el-container>
    <el-header>
      <el-menu
        :default-active="activeIndex2"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
      >
        <el-avatar class="clon" src='https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png'></el-avatar>
        <el-submenu class="fr" index="3">
          <template slot="title">了解网站</template>
          <el-menu-item index="2-1" @click="gouser">作者简介</el-menu-item>
          <el-menu-item index="2-2" @click="goweb">网站简介</el-menu-item>
        </el-submenu>
        <el-menu-item class="fr" index="2" @click="goGit" >GitHub地址</el-menu-item>
        <el-menu-item class="fr" index="1" @click="gomain" >首页</el-menu-item>
      </el-menu>
      <div class="line"></div>
    </el-header>
    <el-container>
      <el-aside width="200px">
        <el-row class="tac">
            <el-menu
              default-active="2"
              class="el-menu-vertical-demo"
              background-color="#545c64"
              @open="handleOpen"
              @close="handleClose"
              text-color="#fff"
              active-text-color="#ffd04b"
            >
              <el-menu-item  @click="movies" index="1">
                <i class="el-icon-video-camera-solid"></i>
                <span slot="title">观影会</span>
              </el-menu-item>
              <el-menu-item  @click="books" index="2">
                <i class="el-icon-s-management"></i>
                <span slot="title">读书会</span>
              </el-menu-item>
              <el-menu-item  @click="technology" index="3">
                <i class="el-icon-star-on"></i>
                <span slot="title">技术栈</span>
              </el-menu-item>
              <el-menu-item  @click="blog" index="4">
                <i class="el-icon-s-flag"></i>
                <span slot="title">技术博客</span>
              </el-menu-item>
              <el-menu-item index="5">
                <i class="el-icon-s-comment"></i>
                <span slot="title">写在最后</span>
              </el-menu-item>
            </el-menu>
        </el-row>
      </el-aside>
      <el-main><router-view/></el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      activeIndex: '1',
      activeIndex2: '1',
      circleUrl: 'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'
    }
  },
  methods: {
    blog () {
      this.$router.push('/Blog').catch(err => { console.log(err) })
    },
    technology () {
      this.$router.push('/Technology').catch(err => { console.log(err) })
    },
    movies () {
      this.$router.push('/Movie').catch(err => { console.log(err) })
    },
    books () {
      this.$router.push('/Book').catch(err => { console.log(err) })
    },
    goGit () {
      this.$router.push('/Git').catch(err => { console.log(err) })
    },
    gomain () {
      this.$router.push('/').catch(err => { console.log(err) })
    },
    goweb () {
      this.$router.push('/Web').catch(err => { console.log(err) })
    },
    gouser () {
      this.$router.push('/User').catch(err => { console.log(err) })
    },
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    },
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style scoped>

.el-container{
  position: absolute;
  width: 100%;
  top: 0px ;
  left: 0 ;
  bottom: 0;
}

.el-header{
  padding: 0;
  z-index: 1000;
}

.el-header .fr{
  float: right;
}

.el-header .el-menu{
  border-bottom: none;
}

.el-aside, .el-main{
  padding-top: 60px;
}

.el-aside{
  background: #545c64;
}

.el-aside .el-menu{
  border-right: none;
}

.clon{
  margin-left: 15px;
  margin-top: 15px;
}
</style>
