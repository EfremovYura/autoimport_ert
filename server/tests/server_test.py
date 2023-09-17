class TestServer:
    def test_get_html(self, test_client):
        response = test_client.get('/html', follow_redirects=True)

        assert response.status_code == 200

    def test_post_json(self, test_client, test_json_data):
        response = test_client.post('/json/', json=test_json_data, follow_redirects=True)

        assert response.status_code == 200
