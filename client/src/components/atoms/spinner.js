
import { SpinnerCircular } from 'spinners-react';

const spinnerStyles = {
    "margin": "50% auto"
}

function Spinner() {
    return (
        <div style={spinnerStyles}>
            <SpinnerCircular color={"white"}/>
        </div>
    );
}

export default Spinner;