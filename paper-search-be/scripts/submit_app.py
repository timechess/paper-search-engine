from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import random
import os

app = Flask(__name__)


# 读取论文数据
def get_random_paper():
    with open("data/iclr.json", "r") as f:
        papers = json.load(f)
    return random.choice(papers)


# 首页
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 处理表单提交
        if "submit_feedback" in request.form:
            submission = {
                "original_id": request.form["original_id"],
                "new_title": request.form["new_title"],
                "new_abstract": request.form["new_abstract"],
                "user_name": request.form["user_name"],
            }
            with open("data/submissions.jsonl", "a") as f:
                f.write(json.dumps(submission, ensure_ascii=False) + "\n")
            return redirect(url_for("index"))

        # 处理“下一篇”请求
        elif "next_paper" in request.form:
            return redirect(url_for("index"))

    # 获取随机论文
    paper = get_random_paper()
    return render_template(
        "index.html",
        title=paper["title"],
        abstract=paper["abstract"],
        paper_id=paper["id"],
    )


# 获取下一篇论文（AJAX 请求）
@app.route("/next", methods=["GET"])
def next_paper():
    paper = get_random_paper()
    return jsonify(
        {
            "title": paper["title"],
            "abstract": paper["abstract"],
            "paper_id": paper["id"],
        }
    )


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    app.run(debug=False)
