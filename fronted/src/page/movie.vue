<template>
  <div class="table">
    <el-table
      :data="movielist"
      style="width: 100%">
    <el-table-column
      label="观影日期"
      width="300">
      <template slot-scope="scope">
        <i class="el-icon-time"></i>
        <span style="margin-left: 10px">{{ scope.row.viewingtime }}</span>
      </template>
    </el-table-column>
    <el-table-column
      label="电影名称"
      width="300">
      <template slot-scope="scope">
        <el-popover trigger="hover" placement="top">
          <p>电影名称: {{ scope.row.moviename }}</p>
          <p>评分: {{ scope.row.moviescore }}</p>
          <p>评语: {{ scope.row.remarks }}</p>
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">{{ scope.row.moviename }}</el-tag>
          </div>
        </el-popover>
      </template>
    </el-table-column>
    <el-table-column
      label="评分"
      width="300">
      <template slot-scope="scope">
        <span style="margin-left: 10px">{{ scope.row.moviescore }}</span>
      </template>
    </el-table-column>
    <el-table-column
      label="评语"
      width="300">
      <template slot-scope="scope">
        <span style="margin-left: 10px">{{ scope.row.remarks }}</span>
      </template>
    </el-table-column>
    <el-table-column label="操作">
      <template slot-scope="scope">
        <el-button
          type="success"
          size="mini"
          @click="handleEdit(scope.row)">观后感</el-button>
      </template>
    </el-table-column>
    </el-table>
    <el-dialog
      :title="impre.title"
      :visible.sync="dialogVisible"
      width="60%"
      :before-close="handleClose"
      center>
    <pre>{{ this.impre.text }}</pre>
    <span slot="footer" class="dialog-footer">
      <el-button @click="dialogVisible = false">关闭</el-button>
    </span>
    </el-dialog>
  </div>
</template>

<script>

export default {
  name: 'Movie',
  data () {
    return {
      movielist: [],
      search: '',
      dialogVisible: false,
      impre: {
        'title': '',
        'text': ''
      }
    }
  },
  mounted () {
    this.getmovielist()
  },
  methods: {
    handleEdit (row) {
      console.log(row)
      this.dialogVisible = true
      this.impre.title = row.moviename
      this.impre.text = row.impressions
    },
    handleClose (done) {
      this.$confirm('确认关闭？')
        .then(_ => {
          done()
        })
        .catch(_ => {})
    },
    getmovielist () {
      this.$axios
        .get('/api/movie')
        .then(response => {
          this.movielist = response.data.querydata
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

</style>
