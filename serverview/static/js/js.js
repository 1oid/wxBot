$("body").css({
    opacity: 1,
    transition: "all 1.5s"
});

function close_or_open_nav(value) {
    $(".book-summary").css({
        width: value,
        transition: "all 0.4s"
    });

    $(".book-body").css({
        left: value,
        transition: "all 0.4s"
    });
}

// 侧边栏的展开与收缩
$(".icon-list").click(function () {
    if($(".book-summary").width() == 300) {
        close_or_open_nav(0);
    }else{
        close_or_open_nav(300);
    }
});

// 点击搜索
$(".icon-search").click(function () {
    if($(".searchbox").height() == 0) {
        $(".searchbox").css({
            height: 40,
            transition: "all 0.4s"
        });
    }else{
        $(".searchbox").css({
            height: 0,
            overflow: "hidden",
            transition: "all 0.4s"
        });
    }
});