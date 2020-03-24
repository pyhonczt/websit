<template>
  <div class="table">
    <el-table
      :data="bloglist"
      style="width: 100%">
    <el-table-column
      label="日期"
      width="400">
      <template slot-scope="scope">
        <i class="el-icon-time"></i>
        <span style="margin-left: 10px">{{ scope.row.blogtime }}</span>
      </template>
    </el-table-column>
    <el-table-column
      label="技术领域"
      width="400">
      <template slot-scope="scope">
        <span style="margin-left: 10px">{{ scope.row.blogtype }}</span>
      </template>
    </el-table-column>
    <el-table-column
      label="简介"
      width="400">
      <template slot-scope="scope">
        <span style="margin-left: 10px">{{ scope.row.remarks }}</span>
      </template>
    </el-table-column>
    <el-table-column label="操作">
      <template slot-scope="scope">
        <el-button
          type="success"
          size="mini"
          @click="handleEdit(scope.row)">详细</el-button>
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
  name: 'Blog',
  data () {
    return {
      bloglist: [],
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
      this.dialogVisible = true
      this.impre.title = row.remarks
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
        .get('/api/blog')
        .then(response => {
          this.bloglist = response.data.querydata
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
