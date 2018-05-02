

1.host 是 echarts js 库的地址，默提供的地址为 https://pyecharts.github.io/assets/js 

2.script_list 是 Page() 类渲染网页所需要依赖的 echarts js 库，依赖的库的数量取决于所要渲染的图形种类。



3.模板扩展

    实际上 {{ myechart|safe }} 封装的是：
    <div id="{{ chart_id }}" style="width:{{ my_width }}px;height:{{ my_height }}px;"></div>
    <script type="text/javascript">
    var myChart_{{ chart_id }} = echarts.init(document.getElementById('{{ chart_id }}'));
    var option_{{ chart_id }} = {{ my_option|safe }};
    myChart_{{ chart_id }}.setOption(option_{{ chart_id }});
    </script>

    可以在路由时传递相应的参数！
