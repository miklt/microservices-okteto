import useSWR from 'swr'
import fetch from "../libs/fetch"
import {useRouter} from 'next/router'
import * as moment from 'moment'
import 'moment/locale/pt-br';

export default function Clima() {
    const router = useRouter()
    const {name} = router.query    
    const { data, error } = useSWR(() => name ? process.env.NEXT_PUBLIC_API_HOST+'/clima?name=' + name:null, fetch)
    if (error) return <div>Erro ao carregar os dados da api</div>
    if (!data) return <div>Carregando dados...</div>
    return (
        <>
            <div className="font-medium">Os dados atualizados vindos na nossa api indicam que em {name} as temperaturas registradas foram de:
            <ul>
                {data.map(t=>formatReading(t))}
            </ul>
            </div>
        </>
    )

}
const formatReading = (reading) => {
    const readingTime  = moment(reading.date).format("DD/MM/YYYY hh:mm:ss")
    return ( <>
    <li>
        {reading.value}º em {readingTime}
    </li>
    </>
    )
}
