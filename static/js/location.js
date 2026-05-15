function getLocation() {

    if (navigator.geolocation) {

        navigator.geolocation.getCurrentPosition(

            function(position) {

                document.getElementById("latitude").value =
                    position.coords.latitude;

                document.getElementById("longitude").value =
                    position.coords.longitude;

                alert(
                    "Location captured successfully!"
                );

                console.log(
                    position.coords.latitude,
                    position.coords.longitude
                );

            },

            function(error) {

                console.log(error);

                if (error.code === 1) {

                    alert(
                        "Location permission denied."
                    );

                } else if (error.code === 2) {

                    alert(
                        "Location unavailable."
                    );

                } else if (error.code === 3) {

                    alert(
                        "Location request timed out."
                    );

                } else {

                    alert(
                        "Unknown location error."
                    );
                }
            }

        );

    } else {

        alert(
            "Geolocation not supported."
        );
    }
}