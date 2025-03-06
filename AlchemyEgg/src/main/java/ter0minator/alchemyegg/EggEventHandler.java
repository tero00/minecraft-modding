package ter0minator.alchemyegg;

import net.minecraft.client.renderer.block.model.ModelResourceLocation;
import net.minecraft.item.Item;
import net.minecraftforge.client.event.ModelRegistryEvent;
import net.minecraftforge.client.model.ModelLoader;
import net.minecraftforge.event.RegistryEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.eventhandler.SubscribeEvent;

@Mod.EventBusSubscriber(modid = Reference.MODID)
public class EggEventHandler {

    @SubscribeEvent
    public static void onModelRegister(ModelRegistryEvent event) {
        // Use the static instance from the Eggs class
        ModelLoader.setCustomModelResourceLocation(Eggs.TRANSMUTED_EGG, 0, new ModelResourceLocation(Eggs.TRANSMUTED_EGG.getRegistryName(), "inventory"));
    }

    @SubscribeEvent
    public static void registerItems(RegistryEvent.Register<Item> event) {
        // Initialize the item

        Eggs.TRANSMUTED_EGG = new TransmutedEgg();
        // Register the item
        event.getRegistry().register(Eggs.TRANSMUTED_EGG);
    }
}
