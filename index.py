from item import Head, Bio, link, Post, Item, Gallery, Tag, award, Moments

head = Head(
    title="Cheryl Shi",
    description="Cheryl 's academic website",
    keywords="Cheryl Shi, Cheryl, Lijie Shi, academic website, personal website",
)

bio = Bio(
    title="Hello, and welcome!",
    image="assets/me.png",
    paragraphs=[
        f"I'm Cheryl Shi, a postgraduate student in {link('HUST','https://www.hust.edu.cn/')} 👩🏻‍🎓 working on thermoelectric materials ⚡, {link('FIRST','https://www.firstinspires.org/robotics/frc')} alumni 🎓 and FRC mentor in team {link('8214 Cyber Unicorn', 'https://www.thebluealliance.com/team/8214')} 🦄",
    ],
    contacts=[
        link("Email", "mailto:cherylslj@gmail.com"),
        link("Instagram", "https://www.instagram.com/cheryl_slj/"),
        link("Github", "https://github.com/cherylslj"),
        link(
            "CNKI",
            "https://kns.cnki.net/kcms2/author/detail?v=At0rObma_qO5Q6Kjsmwk8TjUzFX3KJa4v1D5eTbYNfGhZItRV6q9a9yZtgF1_Qexl9KjLmPUy_zLY41oMbNdUawhOtSvn26aBsakvbgLrOu5Naj-d9T_zw==&uniplatform=NZKPT",
        ),
        link("@Rocky 💕", "https://www.rocky-xrq.com"),
    ],
)

moments = Moments(
    title="🎉 Moments",
    posts=[
        Post(
            date="2024.07.19",
            description="Published a new utility patent in Engineering Science & Technology I",
        ),
        Post(
            date="2024.06.04",
            description=f"Published a new paper in {link('ESST','https://esst.cip.com.cn/CN/2095-4239/home.shtml')}",
        ),
        Post(
            date="2023.08.06",
            description="Champion and industrial design award of FRC 2023 China Off-season",
        ),
    ],
)

_FRC_TAG = Tag(name="FRC", color="0066B3", logo="first")

galleries = [
    Gallery(
        name="🎓 Education",
        items=[
            Item(
                image="assets/hust.jpeg",
                name="Huazhong University of Science and Technology",
                tags=[
                    Tag(name="Wuhan", color="red"),
                    Tag(name="985", color="blue"),
                    Tag(name="211", color="green"),
                ],
                links=[
                    "2023.9 - now",
                    "postgraduate",
                    "Thermoelectric Materials",
                    "School of Energy and Power Engineering",
                ],
            ),
            Item(
                image="assets/usst.png",
                name="University of Shanghai for Science and Technology",
                tags=[
                    Tag(name="Shanghai", color="blue"),
                ],
                links=[
                    "2019.9 - 2023.6",
                    "undergraduate",
                    "Refrigeration and Cryogenic Engineering",
                    "School of Energy and Power Engineering",
                ],
            ),
        ],
    ),
    Gallery(
        name="👔 Internship",
        items=[
            Item(
                image="assets/nextinnovation.png",
                name="Next Innovation",
                tags=[Tag(name="STEM", color="purple")],
                links=["2023.6 - now"],
                description="Mechanical & Scouting Mentor",
                bullets=[
                    "Manage robot development and students training",
                    "Support robot design and assembly",
                    "Conduct competition scouting and data analysis",
                ],
            ),
        ],
    ),
    Gallery(
        name="🤖 Robot",
        items=[
            Item(
                image="assets/82142022.png",
                name="FRC 2022 Robot (Team 8214)",
                tags=[
                    _FRC_TAG,
                    Tag(name="Robotics", color="brightgreen"),
                ],
                links=[
                    award("FRC 2023 China Off-season champion"),
                    award("FRC 2023 China Off-season industrial design award"),
                    "2022.*",
                    link(
                        "Next Innovation STEM Center",
                        "https://github.com/FRCNextInnovation",
                    ),
                    link(
                        "FRC 2022 : RAPID REACT",
                        "https://www.youtube.com/watch?v=LgniEjI9cCM",
                    ),
                    link("Robot Recap", "https://www.bilibili.com/video/BV1iu4y1v7We"),
                ],
            ),
        ],
    ),
    Gallery(
        name="🗃️ Selected Publications",
        items=[
            Item(
                image="assets/snse.png",
                name="Study of heat treatment temperature on the thermoelectric properties of cold-sintered SnSe",
                tags=[
                    Tag(name="SnSe", color="black"),
                    Tag(name="Cold Sintered", color="blue"),
                ],
                links=[
                    "2024.6.4",
                    "Jun Ding, Lijie Shi, Xiangbin Chen, Xiang Qu, Zhe Cheng, Xiufen Li, Man Jiang, Zhiquan Chen, Hongyu Wang",
                    link("HUST", "https://www.hust.edu.cn/"),
                    link("ESST", "https://esst.cip.com.cn/EN/2095-4239/home.shtml"),
                    link(
                        "Full Text",
                        "https://esst.cip.com.cn/EN/10.19799/j.cnki.2095-4239.2024.0501",
                    ),
                ],
            ),
            Item(
                image="assets/shooter.png",
                name="A Ball Collection Mechanism for Robot Ball Shooter",
                tags=[
                    _FRC_TAG,
                    Tag(name="Robotics", color="brightgreen"),
                ],
                links=[
                    "2024.7.19",
                    "Guorui Zhang, Dongmei Zhao, Lijie Shi, Mingfei Zhou, Jinjia Liang, Yibin Hu, Zhiheng Su, Mohan Zhang, Mingzhe Li, Moxun Li",
                    link(
                        "Next Innovation STEM Center",
                        "https://github.com/FRCNextInnovation",
                    ),
                    link(
                        "Full Text",
                        "https://kns.cnki.net/kcms2/article/abstract?v=At0rObma_qNwwOb6DjL51WnNhYvDq4PQaSmqhNYhVGtDDJCoNXuNAgcJ0VT0RxFCRCEr9mM2qk-GtqCBNonPekE7Hpj_6cMSyF1ED_i2YpOIzcLWGenptR5fasM6HUDx0hta9Rsgur6PDDqZ8lKPxWZ51GA2AqmS&uniplatform=NZKPT",
                    ),
                ],
            ),
        ],
    ),
]
