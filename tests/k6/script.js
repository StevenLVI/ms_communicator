import { check } from 'k6';
import http from 'k6/http';
import { FormData } from 'https://jslib.k6.io/formdata/0.0.2/index.js';

// las iteraciones que va tener esta prueba es rate * duration / timeUnit

export const options = {
    scenarios: {
        get_short_url: {
            executor: 'constant-arrival-rate',
            exec: 'get_short_url',
            preAllocatedVUs: 100, // Usuarios concurrentes
            maxVUs: 10000, // Usuarios maximos
            timeUnit: '1s', // Cada cuanto se va hacer el pico de iteraciones
            duration: '30s', // total duration
            rate: 100, // numero de interacciones concurrentes teniendo en cuenta `timeUnit`
        },
    },
};

export function post_short_url () {
    const payload = new FormData();
    payload.append('long_url', 'Lorem');
    payload.append('type_url', 'LANDING');
    payload.append('expiration_date', '2022-01-31');

    const headers = {
        headers: { 'Content-Type': 'multipart/form-data; boundary=' + payload.boundary },
    }
    const res = http.post('http://127.0.0.1:80/v1/short_url/', payload.body(), headers);
    check(res, {
        'Post status is 201': (r) => res.status === 201,
        'Post Transaction time ok': (r) => res.timings.duration < 1000,
    });
}

export function get_short_url () {

    const res = http.get('http://127.0.0.1:80/v1/short_url/yB5xL/redirect/');
    check(res, {
        'Get status is 200': (r) => res.status === 200,
        'Get Transaction time ok': (r) => res.timings.duration < 1000,
    });
}