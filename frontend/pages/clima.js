import useSWR from 'swr'
import fetch from "../libs/fetch";
export default function Clima() {
    const { data, error } = useSWR(process.env.NEXT_PUBLIC_API_HOST+'/', fetch)
    if (error) return <div>Erro ao carregar os dados da api</div>
    if (!data) return <div>Carregando dados...</div>
    return <>
        <div>Os dados vindos na nossa api indicam que a temperatura às {data.hour} em {data.city} eram de: {data.temperature}º</div>
        </>
}