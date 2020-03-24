<template>
<div class="table">
  <el-card class="box-card">
    <i class="el-icon-info">说明 :</i>
    <el-tooltip class="items" effect="dark" content="能读懂他人代码并复刻简单功能" placement="bottom">
      <el-tag>20%</el-tag>
    </el-tooltip>
    <el-tooltip class="items" effect="dark" content="能独立编写出较为复杂的功能" placement="bottom">
      <el-tag type="success">40%</el-tag>
    </el-tooltip>
    <el-tooltip class="items" effect="dark" content="熟练掌握此项技术并能写出很复杂的功能" placement="bottom">
      <el-tag type="info">60%</el-tag>
    </el-tooltip>
    <el-tooltip class="items" effect="dark" content="深入阅读并理解过源码并能在现有基础上进行新的功能扩展" placement="bottom">
      <el-tag type="warning">80%</el-tag>
    </el-tooltip>
    <el-tooltip class="items" effect="dark" content="终极技术大牛不解释" placement="bottom">
      <el-tag type="danger">100%</el-tag>
    </el-tooltip>
    <el-divider></el-divider>
    <div v-for="o in technologylist" :key="o.id" class="text item">
      {{ o.technologyname }}
      <el-progress v-if="o.technologyscore < 20" :percentage="o.technologyscore" :color="customColorfri"></el-progress>
      <el-progress v-else-if="20 <= o.technologyscore && o.technologyscore < 40" :percentage="o.technologyscore" :color="customColorsec"></el-progress>
      <el-progress v-else-if="40 <= o.technologyscore && o.technologyscore < 60" :percentage="o.technologyscore" :color="customColorthr"></el-progress>
      <el-progress v-else-if="60 <= o.technologyscore && o.technologyscore < 80" :percentage="o.technologyscore" :color="customColorfour"></el-progress>
      <el-progress v-else-if="80 <= o.technologyscore && o.technologyscore <= 100" :percentage="o.technologyscore" :color="customColorfive"></el-progress>
    </div>
  </el-card>
</div>
</template>

<script>

export default {
  name: 'Technology',
  data () {
    return {
      customColorfri: '#f56c6c',
      customColorsec: '#e6a23c',
      customColorthr: '#5cb87a',
      customColorfour: '#1989fa',
      customColorfive: '#6f7ad3',
      technologylist: []
    }
  },
  mounted () {
    this.getmovielist()
  },
  methods: {
    getmovielist () {
      this.$axios
        .get('/api/technology')
        .then(response => {
          this.technologylist = response.data.querydata
        })
        .catch(response => {
          console.log('error')
        })
    }
  }
}
</script>

<style scoped>
  .el-container {
    padding: 0px;
    margin: 0px;
  }
  .el-main {
    padding: 0px;
    margin: 0px;
  }
  .el-header {
    padding: 0px;
    margin: 0px;
  }
  .el-aside {
    padding: 0px;
    margin: 0px;
  }
  .table {
    margin-top: 10px;
    margin-left: 10px;
  }
  .text {
    font-size: 14px;
  }

  .item {
    padding: 18px 0;
  }

  .items {
    margin: 4px;
  }

  .box-card {
    width: 1350px;
  }

</style>
