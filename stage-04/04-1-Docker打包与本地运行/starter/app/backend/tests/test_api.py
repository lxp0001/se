def test_list_events(client):
    response = client.get("/events")

    assert response.status_code == 200
    assert response.json()
    assert response.json()[0]["name"]


# TODO 1：编写新增测试。
# 提示：POST /events/1/registrations，JSON 为 {"username": "user1"}；
# 检查 201、返回的用户名，并 GET 列表确认记录能读回来。


# TODO 2：编写修改测试。
# 提示：先新增一条报名，从响应中取 id；PATCH 对应网址，把用户名改成 user2；检查 200 和新用户名。


# TODO 3：编写删除测试。
# 提示：先新增一条报名，从响应中取 id；DELETE 对应网址；检查 204，再 GET 列表确认为空。
