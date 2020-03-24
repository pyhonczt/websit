<template>
  <div class="table">
    <el-table
      :data="booklist"
      style="width: 100%">
    <el-table-column
      label="开始日期"
      width="250">
      <template slot-scope="scope">
        <i class="el-icon-time"></i>
        <span style="margin-left: 10px">{{ scope.row.booktimestart }}</span>
      </template>
    </el-table-column>
    <el-table-column
      label="结束日期"
      width="250">
      <template slot-scope="scope">
        <i class="el-icon-time"></i>
        <span style="margin-left: 10px">{{ scope.row.booktimeend }}</span>
      </template>
    </el-table-column>
    <el-table-column
      label="书名"
      width="250">
      <template slot-scope="scope">
        <el-popover trigger="hover" placement="top">
          <p>书名: {{ scope.row.bookname }}</p>
          <p>理解度: {{ scope.row.bookscore }}</p>
          <p>评语: {{ scope.row.remarks }}</p>
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">{{ scope.row.bookname }}</el-tag>
          </div>
        </el-popover>
      </template>
    </el-table-column>
    <el-table-column
      label="评分"
      width="250">
      <template slot-scope="scope">
        <span style="margin-left: 10px">{{ scope.row.bookscore }}</span>
      </template>
    </el-table-column>
    <el-table-column
      label="评语"
      width="250">
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
  name: 'Book',
  data () {
    return {
      booklist: [],
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
      this.impre.title = row.bookname
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
        .get('/api/book')
        .then(response => {
          this.booklist = response.data.querydata
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
