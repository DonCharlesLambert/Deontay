import React from "react";
import { Chart } from "react-google-charts";

export const options = {
  legend: "none",
  bar: { groupWidth: "40%" },
  candlestick: {
    fallingColor: { strokeWidth: 0, fill: "#a52714" },
    risingColor: { strokeWidth: 0, fill: "#0f9d58" },
  },
  fontColor: "white",
  backgroundColor: "transparent",
};

function CandlestickChart({data}) {
  console.log(data.length)
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
