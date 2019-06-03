module.exports = {
    devServer: {
        proxy: {
            '^/v1': {
                target: 'http://localhost:8081',
                changeOrigin: true
            }
        }
    }
};