function ReturnArrow({change}) {
  const changeClass = change < 0 ? "panelNegative" : "panelPositive"
  const changeArrow = change < 0 ? "▼" : "▲"
  const changeSign = change < 0 ? "" : "+"
  return (
    <p className={`assertReturnsChange ${changeClass}`}> {changeArrow} {changeSign}{change}% </p>
  );
}

export default ReturnArrow;