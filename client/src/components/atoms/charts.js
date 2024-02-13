import React from "react";
import { Chart } from "react-google-charts";

export const options = {
  legend: "none",
  hAxis: {
    textStyle:{color: '#FFF'}
  },
  vAxis: {
    textStyle:{color: '#FFF'}
  },
  color: "white",
  backgroundColor: "transparent",
};

function CandlestickChart({data}) {
  return (
    <Chart
      chartType="LineChart"
      width="100%"
      height="100%"
      data={data}
      options={options}
    />
  );
}

export default CandlestickChart;
