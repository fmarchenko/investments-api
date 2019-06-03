<template>
    <section class="calculate-view">
        <div class="container">
            <h1 class="border-bottom mb-4">Calculate Investments Performance</h1>
            <div class="row">
                <div class="col-12">
                    <form class="mb-4" @submit.prevent="handleSubmit">
                        <div class="form-row align-items-center">
                            <div class="col-auto">
                                <label for="id_start_date" class="sr-only">Investments start date</label>
                                <input type="date" class="form-control mb-2" id="id_start_date"
                                       placeholder="Investments start date" v-model="start_date" required>
                            </div>
                            <div class="col-auto">
                                <label for="id_amount" class="sr-only">Investments amount in USD</label>
                                <input type="number" class="form-control mb-2" id="id_amount"
                                       placeholder="Investments amount" v-model="amount">
                            </div>
                            <div class="col-auto">
                                <button type="submit" class="btn btn-primary mb-2" id="id_send">Calculate</button>
                            </div>
                        </div>
                    </form>
                </div>
                <div class="col-12 text-center" v-if="loading">
                    <p class="spinner-border" style="width: 3rem; height: 3rem;"><span class="sr-only">Loading...</span></p>
                </div>
                <div class="col-12" v-if="result.length > 0 && !loading">
                    <ul class="nav nav-tabs" role="tablist">
                        <li v-for="(item, index) in result" v-bind:key="index" class="nav-item">
                            <a v-bind:href="'#'+item.asset" class="nav-link" v-bind:class="{ active: index == 0 }"
                               role="tab" data-toggle="tab">{{ item.asset }}</a>
                        </li>
                    </ul>
                    <div class="tab-content">
                        <div class="tab-pane fade" v-for="(item, index) in result" v-bind:key="index"
                             v-bind:class="{ 'show active': index == 0 }" role="tabpanel" v-bind:id="item.asset">
                            <h3 class="pt-3 pb-3">Investment: #{{ item.investment }} start from {{ new Date(item.open_date).toDateString() }}
                                <br>
                                <small class="text-muted">on {{ item.amount }} USD</small>
                            </h3>
                            <table class="table table-striped">
                                <thead>
                                <tr>
                                    <th>#</th>
                                    <th>Month</th>
                                    <th>Profit, USD</th>
                                    <th>Month Profitability, %</th>
                                    <th>Total Profitability, %</th>
                                </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(performance, index) in item.performances" v-bind:key="index">
                                        <td>{{ index }}</td>
                                        <td>{{ new Date(performance.day).toDateString() }}</td>
                                        <td>{{ performance.profit }}</td>
                                        <td>{{ performance.profitability }}</td>
                                        <td>{{ performance.profitability_total }}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'CalcView',
        data() {
            return {
                loading: false,
                start_date: '2017-09-01',
                amount: 1000,
                result: []
            }
        },
        methods: {
            handleSubmit(){
                let start_date = new Date(this.start_date);
                let url = `/api/v1/performance/${start_date.getFullYear()}/${start_date.getMonth() + 1}/${start_date.getUTCDate()}/`;
                if(this.amount > 0){
                    url += `${this.amount}/`
                }
                this.loading = true;
                axios.get(url).then(response => {
                    this.result = response.data.result;
                    this.loading = false;
                });
            }
        }
    }
</script>