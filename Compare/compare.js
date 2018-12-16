var figure = {
    "frames": [], 
    "layout": {
        "autosize": true, 
        "title": "Compare a number of tweets between #ICONSIAM and 'Apple Store'", 
        "dragmode": "pan", 
        "colorway": [
            "#66c2a5", 
            "#fc8d62", 
            "#8da0cb", 
            "#e78ac3", 
            "#a6d854", 
            "#ffd92f", 
            "#e5c494", 
            "#b3b3b3"
        ], 
        "yaxis": {
            "range": [
                0, 
                141.05263157894737
            ], 
            "type": "linear", 
            "autorange": true, 
            "title": "Number of tweets"
        }, 
        "xaxis": {
            "range": [
                -0.5, 
                11.5
            ], 
            "type": "category", 
            "autorange": true, 
            "title": "Date"
        }, 
        "hovermode": "x"
    }, 
    "data": [
        {
            "name": "#ICONSIAM", 
            "ysrc": "ksankaseam:4:120177", 
            "xsrc": "ksankaseam:4:ff4c99", 
            "stackgroup": 1, 
            "mode": "lines", 
            "decreasing": {
                "line": {
                    "color": "#7f7f7f"
                }
            }, 
            "y": [
                "8", 
                "44", 
                "73", 
                "100", 
                "134", 
                "47", 
                "40", 
                "56", 
                "104", 
                "48", 
                "75", 
                "40"
            ], 
            "x": [
                "27-Nov", 
                "28-Nov", 
                "29-Nov", 
                "30-Nov", 
                "01-Dec", 
                "02-Dec", 
                "03-Dec", 
                "04-Dec", 
                "05-Dec", 
                "06-Dec", 
                "07-Dec", 
                "08-Dec"
            ], 
            "increasing": {
                "line": {
                    "color": "#17becf"
                }
            }, 
            "type": "bar", 
            "orientation": "v"
        }, 
        {
            "name": "Apple Store", 
            "ysrc": "ksankaseam:4:b5fe42", 
            "xsrc": "ksankaseam:4:ff4c99", 
            "stackgroup": 1, 
            "mode": "lines", 
            "y": [
                "1", 
                "2", 
                "1", 
                "", 
                "4", 
                "2", 
                "1", 
                "", 
                "5", 
                "2", 
                "3"
            ], 
            "x": [
                "27-Nov", 
                "28-Nov", 
                "29-Nov", 
                "30-Nov", 
                "01-Dec", 
                "02-Dec", 
                "03-Dec", 
                "04-Dec", 
                "05-Dec", 
                "06-Dec", 
                "07-Dec", 
                "08-Dec"
            ], 
            "type": "bar", 
            "orientation": "v"
        }
    ]
}